/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javaapplication7;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;

/**
 *
 * @author naika
 */
public class hello {
    public static void main(String[] args) {
        // Set the path to the ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "D:\\DEVOPS LAB\\WebDrivers\\chromedriver.exe");

        // Initialize ChromeDriver
        WebDriver driver = new EdgeDriver();

        try {
            // Open a website
            driver.get("C://Users//naika//Downloads//Website//home.html");

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
