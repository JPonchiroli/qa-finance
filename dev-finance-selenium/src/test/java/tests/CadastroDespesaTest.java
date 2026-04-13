package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.*;

import java.time.Duration;

public class CadastroDespesaTest {

    private WebDriver driver;
    private WebDriverWait wait;

    @BeforeEach
    void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();

        wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        driver.get("https://dev-finance.netlify.app");
    }

    @Test
    void deveCadastrarDespesaComSucesso() {

        WebElement botaoNovaTransacao = wait.until(
                ExpectedConditions.elementToBeClickable(By.cssSelector("a.button.new"))
        );
        botaoNovaTransacao.click();

        WebElement descricao = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("description"))
        );
        descricao.sendKeys("Teste Selenium");

        WebElement valor = driver.findElement(By.id("amount"));
        valor.sendKeys("-500");

        WebElement data = driver.findElement(By.id("date"));
        data.sendKeys("2026-04-13");

        WebElement botaoSalvar = driver.findElement(
                By.xpath("//button[text()='Salvar']")
        );
        botaoSalvar.click();

        WebElement tabela = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("data-table"))
        );

        Assertions.assertTrue(
                tabela.getText().contains("Teste Selenium"),
                "A despesa não foi cadastrada com sucesso!"
        );
    }

    @AfterEach
    void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
