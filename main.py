import csv
import asyncio
from playwright.async_api import async_playwright

async def scrape_hospitals():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=False, 
            executable_path="/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
        )
        page = await browser.new_page()

        await page.goto("https://www.google.com/search?q=medical+hospitals+in+england&sca_esv=d0a8b3810471bc0b&biw=1706&bih=919&tbm=lcl&sxsrf=ADLYWIKKqiKp-IJmUCt5C93Fle2k0slh_w%3A1732896544816&ei=IOdJZ62bMe7o7_UPirWfkAs&oq=Medical+hospitals+in+scottland&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIh5NZWRpY2FsIGhvc3BpdGFscyBpbiBzY290dGxhbmQqAggAMgcQIRigARgKMgcQIRigARgKSMewClDvmQpYlqcKcAB4AJABAJgBlQKgAf4TqgEEMi0xMLgBA8gBAPgBAZgCCqAClhTCAgcQIxiwAhgnwgIGEAAYFhgewgILEAAYgAQYhgMYigXCAgUQIRigAcICBBAhGBWYAwCIBgGSBwQyLTEwoAepOg&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[58.76229060000001,-2.2753929999999998],[55.423666399999995,-5.2645555]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2")

        output_file = "England_hospitals_data.csv"

        headers = ["Institute Name", "Institute Type", "Location", "Total Rating", "Phone Number", "Website Link"]

        with open(output_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)

            while True:
                await page.wait_for_timeout(5000)

                hospitals = await page.query_selector_all("div[jscontroller='AtSb']")
                for hospital in hospitals:
                    institute_name = await hospital.query_selector("div[aria-level='3']")
                    institute_name = await institute_name.inner_text() if institute_name else "N/A"

                    institute_type = await hospital.query_selector("div:nth-of-type(2)")
                    institute_type_text = await institute_type.inner_text() if institute_type else "N/A"
                    institute_type = institute_type_text.split("·")[1].strip() if "·" in institute_type_text else "N/A"

                    location = await hospital.query_selector("div:nth-of-type(3)")
                    location = await location.inner_text() if location else "N/A"

                    total_rating = await hospital.query_selector("span[aria-label^='Rated']")
                    total_rating = await total_rating.inner_text() if total_rating else "N/A"

                    phone_number = await hospital.query_selector("div:nth-of-type(4)")
                    phone_number_text = await phone_number.inner_text() if phone_number else "N/A"
                    phone_number = phone_number_text.split("·")[1].strip() if "·" in phone_number_text else "N/A"

                    website_link = await hospital.query_selector("a[href^='http']")
                    website_link = await website_link.get_attribute("href") if website_link else "N/A"

                    writer.writerow([institute_name, institute_type, location, total_rating, phone_number, website_link])

                next_button = await page.query_selector("a#pnnext")
                if next_button:
                    await next_button.click()
                else:
                    print("No more pages to scrape.")
                    break

        print(f"Data has been saved to {output_file}")
        await browser.close()

asyncio.run(scrape_hospitals())
