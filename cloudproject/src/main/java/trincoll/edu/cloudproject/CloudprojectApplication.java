package trincoll.edu.cloudproject;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import trincoll.edu.ui.homepage;
import trincoll.edu.restaction.image_up;

@RestController
@SpringBootApplication(exclude={DataSourceAutoConfiguration.class})
public class CloudprojectApplication {

	public static void main(String[] args) {
		SpringApplication.run(CloudprojectApplication.class, args);
		//homepage hp = new homepage();
	}

	@GetMapping("/")
	public String homePage(){
		homepage hp = new homepage();
		
		return hp.home();
	}

	@GetMapping("/image")
	public String getImage(){
		image_up ra = new image_up();

		return ra.getResponse("test.jpg");
	}
}
