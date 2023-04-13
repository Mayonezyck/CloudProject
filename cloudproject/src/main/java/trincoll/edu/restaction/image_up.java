package trincoll.edu.restaction;

import org.springframework.web.client.RestTemplate;

public class image_up {
    public String getResponse(String imagePath){
        RestTemplate geter = new RestTemplate();
        String apiurl = "http://34.71.86.112:5000/model/metadata";
        String apiresponse = geter.getForObject(apiurl, String.class);
        return apiresponse;
    }
}
