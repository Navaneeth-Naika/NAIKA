/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */


import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;

/**
 *
 * @author naika
 */
public class JavaApplication7 {

    /**
     * @param args the command line arguments
     */
        public static void main(String[] args) {
        // Set the path to the ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "D:\\DEVOPS LAB\\WebDrivers\\chromedriver.exe");

        // Initialize ChromeDriver
        WebDriver driver = new EdgeDriver();

        try {
            // Open a website
            driver.get("https://www.google.com");

            // Print the title of the page
            System.out.println("Title: " + driver.getTitle());

            // Wait for 60 seconds
            Thread.sleep(60000);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            // Close the browser
            driver.quit();
        }
    }

    
}
