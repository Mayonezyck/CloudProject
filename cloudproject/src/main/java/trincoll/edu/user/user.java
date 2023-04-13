package trincoll.edu.user;

import java.util.Objects;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@SuppressWarnings("JpaDataSourceORMInspection")
@Entity
public class user {
    
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer userID;

    public user() {}
    
    public Integer getID() {
        return this.userID;
    }
}
