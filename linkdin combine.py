from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

# Configuration
USERNAME = 'ahmedfarooq3200012@gmail.com'
PASSWORD = 'ga3323700012'
CSV_INPUT_FILE = r'D:\\Arslan testing Data\\Linkdin\\fixed_profiles.csv'  # Input CSV file path
EXCEL_OUTPUT_FILE = r'D:\\Arslan testing Data\\linkdin\\scraped_profiles.xlsx'  # Output Excel file path
# Update with the path to your ChromeDriver

# Initialize the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome()

# Prepare lists to store the scraped data
data_list = []
error_list = []

try:
    # Go to LinkedIn login page
    driver.get('https://www.linkedin.com/login')
    time.sleep(10)

    # Log in to LinkedIn
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)

    # Read profiles from the CSV
    try:
        profiles_df = pd.read_csv(CSV_INPUT_FILE, encoding='ISO-8859-1')
        if 'profile_url' not in profiles_df.columns:
            raise ValueError("The CSV file does not contain a 'profile_url' column.")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        driver.quit()
        exit()

    # Loop through each profile in the CSV
    for index, row in profiles_df.iterrows():
        profile_url = row.get('profile_url', '').strip()
        if not profile_url:
            error_list.append({'Index': index, 'Error': 'Missing profile URL'})
            continue

        # Open the profile URL directly in the current tab
        try:
            driver.get(profile_url)
            time.sleep(5)  # Wait for the profile page to load completely
        except Exception as e:
            error_list.append({'Profile URL': profile_url, 'Error': f"Failed to open profile: {e}"})
            continue

        # Initialize variables to catch the scraped data
        profile_data = {'Profile URL': profile_url, 'Name': '', 'Location': '', 'Headline': '', 'About Us': '',
                        'Experience': '', 'Skills': '', 'Education': '', 'Profile Picture': '', 'Error': ''}

        try:
            # Scrape the name
            name = driver.find_element(By.CSS_SELECTOR, 'h1').text
            profile_data['Name'] = name
        except NoSuchElementException:
            profile_data['Name'] = "Not Found"

        try:
            headline = driver.find_element(By.XPATH, "//h2[contains(@class, 'top-card-layout__headline')]").text
            profile_data['Headline'] = headline
        except NoSuchElementException:
            profile_data['Headline'] = "Not Found"

        try:
            location_per = driver.find_element(By.XPATH, "//div[@class='not-first-middot']/span[1]").text
            profile_data['Location'] = location_per
        except NoSuchElementException:
            profile_data['Location'] = "Not Found"

        try:
            profile_picture = driver.find_element(By.XPATH,
                                                  "//img[contains(@class, 'top-card__profile-image') and contains(@class, 'lazy-loaded')]").get_attribute(
                'src')
            profile_data['Profile Picture'] = profile_picture
        except NoSuchElementException:
            profile_data['Profile Picture'] = "Not Found"

        try:
            about = driver.find_element(By.XPATH,
                                        "//div[contains(@class, 'core-section-container__content') and contains(@class, 'break-words')]/p").text
            profile_data['About Us'] = about
        except NoSuchElementException:
            profile_data['About Us'] = "Not Found"

        # ---------------------------------------Experience-----------------------------------------------
        try:
            experience_sections = driver.find_elements(By.XPATH,
                                                       "//section[contains(@class, 'experience')]//ul[contains(@class, 'experience__list')]/li")
            experiences = []

            for section in experience_sections:
                try:
                    roles = section.find_elements(By.XPATH, ".//div[contains(@class, 'pl-0.5 grow break-words')]")
                    if roles:
                        company_name = section.find_element(By.XPATH,
                                                            ".//span[@class='experience-item__subtitle']").text
                        for role in roles:
                            try:
                                job_title = role.find_element(By.XPATH, ".//span[@class='experience-item__title']").text
                                date_range = role.find_element(By.XPATH, ".//span[contains(@class, 'date-range')]").text
                                location_elements = role.find_elements(By.XPATH,
                                                                       ".//p[contains(@class, 'experience-item__meta-item')]")
                                location = location_elements[-1].text if location_elements else "N/A"
                                experiences.append(f"{job_title} at {company_name} ({date_range}, {location})")
                            except Exception as role_error:
                                print(f"Error processing role: {role_error}")
                    else:
                        try:
                            job_title = section.find_element(By.XPATH, ".//span[@class='experience-item__title']").text
                            company_name = section.find_element(By.XPATH,
                                                                ".//span[@class='experience-item__subtitle']").text
                            date_range = section.find_element(By.XPATH, ".//span[contains(@class, 'date-range')]").text
                            location_elements = section.find_elements(By.XPATH,
                                                                      ".//p[contains(@class, 'experience-item__meta-item')]")
                            location = location_elements[-1].text if location_elements else "N/A"
                            experiences.append(f"{job_title} at {company_name} ({date_range}, {location})")
                        except Exception as single_role_error:
                            print(f"Error processing single role: {single_role_error}")

                except Exception as section_error:
                    print(f"Error processing section: {section_error}")
            profile_data['Experience'] = "\n".join(experiences) if experiences else "No experience found."
        except Exception as e:
            profile_data['Experience'] = f"Experience extraction failed. Error: {str(e)}"

        # ---------------------------------------Education-----------------------------------------------
        try:
            education_items = driver.find_elements(By.XPATH, "//li[contains(@class, 'education__list-item')]")
            education = []

            for item in education_items:
                try:
                    university_name = item.find_element(By.XPATH, ".//h3/a").text
                except:
                    university_name = "N/A"

                try:
                    associated_institute_or_degree = item.find_element(By.XPATH, ".//h4/span[1]").text
                except:
                    associated_institute_or_degree = "N/A"

                try:
                    degree_or_field = item.find_element(By.XPATH, ".//span[@data-section='educations']").text
                except:
                    degree_or_field = "N/A"

                try:
                    date_range = item.find_element(By.XPATH, ".//span[contains(@class, 'date-range')]").text
                except:
                    date_range = "N/A"

                education.append(
                    f"{university_name} - {associated_institute_or_degree} ({degree_or_field}) [{date_range}]")

            profile_data['Education'] = "\n".join(education) if education else "No education details found."
        except Exception as e:
            profile_data['Education'] = f"Education extraction failed. Error: {str(e)}"

        # ---------------------------------------Skills-----------------------------------------------
        skills_elements = driver.find_elements(By.CSS_SELECTOR, '.pv-skill-category-entity__name-text')
        skills = [skill.text for skill in skills_elements if skill.text]
        profile_data['Skills'] = ', '.join(skills)

        # Append the profile data to the list
        data_list.append(profile_data)

    # Create a DataFrame to store the results
    results_df = pd.DataFrame(data_list)

    # Save the results to an Excel file
    results_df.to_excel(EXCEL_OUTPUT_FILE, index=False)

except Exception as e:
    print(f"An error occurred during the process: {e}")

finally:
    driver.quit()
    print(f"Scraping completed. Results saved to {EXCEL_OUTPUT_FILE}.")
