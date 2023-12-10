package dev.alien.alienintelligenceagency;

import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;

import dev.alien.alienintelligenceagency.enums.MissionType;
import dev.alien.alienintelligenceagency.models.Agent;

import dev.alien.alienintelligenceagency.models.Mission;
import net.minidev.json.JSONArray;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.test.annotation.DirtiesContext;

import java.net.http.HttpRequest;

import static org.assertj.core.api.Assertions.assertThat;


@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@DirtiesContext(classMode = DirtiesContext.ClassMode.AFTER_EACH_TEST_METHOD)
public class MissionControllerTests {

    @Autowired
    private TestRestTemplate restTemplate;


    @BeforeEach
    void agentSetUp() {

        Agent agent = new Agent(null, "Mr. Humili", 54);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/agent", agent, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);
    }

    @Test
    void shouldCreateANewMission() {

        Mission mission = new Mission(null, MissionType.CIVIC_ACTION, "Wow the lord", 1L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);
    }

    @Test
    void shouldNotCreateANewMission() {

        Mission mission = new Mission(null, MissionType.CIVIC_ACTION, "Wow the lord", 3L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.UNPROCESSABLE_ENTITY);

        ResponseEntity<String> postResponse2 = this.restTemplate.postForEntity("/mission", null, String.class);
        assertThat(postResponse2.getStatusCode()).isEqualTo(HttpStatus.UNSUPPORTED_MEDIA_TYPE);
    }

    @Test
    void shouldReturnAMissionById() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission/1", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);
        DocumentContext docContext = JsonPath.parse(getResponse.getBody());

        //ID
        Number id = docContext.read("$.id");
        assertThat(id).isEqualTo(1);

        //TYPE
        String type = docContext.read("$.type");
        assertThat(type).isEqualTo(MissionType.SPECIAL_RECONNAISSANCE.name());

        //NAME
        String name = docContext.read("$.name");
        assertThat(name).isEqualTo("Blue Yeti");

        //AGENT ID
        Number agentId = docContext.read("$.agentId");
        assertThat(agentId).isEqualTo(1);
    }

    @Test
    void shouldNotReturnAMission() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission/3", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.NOT_FOUND);

        ResponseEntity<String> getResponse2 = this.restTemplate.getForEntity("/mission/f", String.class);
        assertThat(getResponse2.getStatusCode()).isEqualTo(HttpStatus.BAD_REQUEST);
    }

    @Test
    void shouldReturnAllMissions() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);
        DocumentContext docContext = JsonPath.parse(getResponse.getBody());

        //MISSION COUNT
        int missionCount = docContext.read("$.length()");
        assertThat(missionCount).isEqualTo(1);

        //IDS
        JSONArray ids = docContext.read("$..id");
        assertThat(ids).containsExactlyInAnyOrder(1);

        //TYPES
        JSONArray types = docContext.read("$..type");
        assertThat(types).containsExactlyInAnyOrder(MissionType.SPECIAL_RECONNAISSANCE.name());

        //NAMES
        JSONArray names = docContext.read("$..name");
        assertThat(names).containsExactlyInAnyOrder("Blue Yeti");

        //AGENT IDS
        JSONArray agentIds = docContext.read("$..agentId");
        assertThat(agentIds).containsExactlyInAnyOrder(1);
    }

    @Test
    void shouldUpdateMissionAgentId() {

        Agent agent = new Agent(null, "Mr. Cactus", 36);
        ResponseEntity<String> agentPostResponse = this.restTemplate.postForEntity("/agent", agent, String.class);
        assertThat(agentPostResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);
        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> putResponse = this.restTemplate.exchange("/mission/1/2", HttpMethod.PUT, null, String.class);
        assertThat(putResponse.getStatusCode()).isEqualTo(HttpStatus.NO_CONTENT);

        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission/1", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);
        DocumentContext docContext = JsonPath.parse(getResponse.getBody());

        //AGENT ID
        Number agentId = docContext.read("$.agentId");
        assertThat(agentId).isEqualTo(2);

    }

    @Test
    void shouldNotUpdateMissionAgentId() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> putResponse = this.restTemplate.exchange("/mission/1/3", HttpMethod.PUT, null, String.class);
        assertThat(putResponse.getStatusCode()).isEqualTo(HttpStatus.UNPROCESSABLE_ENTITY);
    }

    @Test
    void shouldDeleteAMissionById() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> deleteResponse = this.restTemplate.exchange("/mission/1", HttpMethod.DELETE, null, String.class);
        assertThat(deleteResponse.getStatusCode()).isEqualTo(HttpStatus.NO_CONTENT);

        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission/1", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.NOT_FOUND);
    }

    @Test
    void shouldNotDeleteAMission() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);

        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> deleteResponse = this.restTemplate.exchange("/mission/2", HttpMethod.DELETE, null, String.class);
        assertThat(deleteResponse.getStatusCode()).isEqualTo(HttpStatus.NO_CONTENT);

        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission/1", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);
    }

    @Test
    void shouldDeleteAllMissionByAgentId() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);
        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);

        Mission mission2 = new Mission(null, MissionType.COUNTER_TERRORISM, "Orange with sunglasses", 1L);
        ResponseEntity<String> postResponse2 = this.restTemplate.postForEntity("/mission", mission2, String.class);
        assertThat(postResponse2.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> deleteResponse = this.restTemplate.exchange("/mission/all/1", HttpMethod.DELETE, null, String.class);
        assertThat(deleteResponse.getStatusCode()).isEqualTo(HttpStatus.NO_CONTENT);

        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission/1", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.NOT_FOUND);

        ResponseEntity<String> getResponse2 = this.restTemplate.getForEntity("/mission/2", String.class);
        assertThat(getResponse2.getStatusCode()).isEqualTo(HttpStatus.NOT_FOUND);
    }

    @Test
    void shouldNotDeleteAllMissions() {

        Mission mission = new Mission(null, MissionType.SPECIAL_RECONNAISSANCE, "Blue Yeti", 1L);
        ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/mission", mission, String.class);
        assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);

        Mission mission2 = new Mission(null, MissionType.COUNTER_TERRORISM, "Orange with sunglasses", 1L);
        ResponseEntity<String> postResponse2 = this.restTemplate.postForEntity("/mission", mission2, String.class);
        assertThat(postResponse2.getStatusCode()).isEqualTo(HttpStatus.CREATED);


        ResponseEntity<String> deleteResponse = this.restTemplate.exchange("/mission/all/2", HttpMethod.DELETE, null, String.class);
        assertThat(deleteResponse.getStatusCode()).isEqualTo(HttpStatus.NO_CONTENT);

        ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/mission/1", String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);

        ResponseEntity<String> getResponse2 = this.restTemplate.getForEntity("/mission/2", String.class);
        assertThat(getResponse2.getStatusCode()).isEqualTo(HttpStatus.OK);

    }

}
