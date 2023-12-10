package dev.alien.alienintelligenceagency;

import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;

import dev.alien.alienintelligenceagency.models.Agent;

import net.minidev.json.JSONArray;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.test.annotation.DirtiesContext;

import static org.assertj.core.api.Assertions.assertThat;


@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@DirtiesContext(classMode = DirtiesContext.ClassMode.AFTER_EACH_TEST_METHOD)
class AgentControllerTests {

	@Autowired
	private TestRestTemplate restTemplate = null;


	@Test
	void shouldCreateANewAgent() {

		Agent agent = new Agent(null, "Joshua", 32);

		ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/agent", agent, String.class);
		assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);

	}

	@Test
	void shouldNotCreateANewAgentWhenIsNotValid() {

		Agent agent = new Agent(null, null, 23);

		ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/agent", agent, String.class);
		assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.INTERNAL_SERVER_ERROR);

		ResponseEntity<String> postResponse2 = this.restTemplate.postForEntity("/agent", null, String.class);
		assertThat(postResponse2.getStatusCode()).isEqualTo(HttpStatus.UNSUPPORTED_MEDIA_TYPE);
	}

	@Test
	void shouldReturnAnAgentById() {

		Agent agent = new Agent(1L, "Jack", 19);

		ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/agent", agent, String.class);
		assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


		ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/agent/1", String.class);
		assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);
		DocumentContext docContext = JsonPath.parse(getResponse.getBody());

		//ID
		Number id = docContext.read("$.id");
		assertThat(id).isEqualTo(1);

		//NAME
		String name = docContext.read("$.name");
		assertThat(name).isEqualTo("Jack");

		//AGE
		Integer age = docContext.read("$.age");
		assertThat(age).isEqualTo(19);
	}

	@Test
	void shouldNotReturnAgentByWrongId() {

		Agent agent = new Agent(1L, "Jack", 19);

		ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/agent", agent, String.class);
		assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);

		ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/agent/2", String.class);
		assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.NOT_FOUND);

	}

	@Test
	void shouldReturnAllAgents() {

		Agent agent = new Agent(1L, "Jack", 19);

		ResponseEntity<String> postResponse = this.restTemplate.postForEntity("/agent", agent, String.class);
		assertThat(postResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);


		ResponseEntity<String> getResponse = this.restTemplate.getForEntity("/agent", String.class);
		assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);
		DocumentContext docContext = JsonPath.parse(getResponse.getBody());

		//LIST LENGTH
		int length = docContext.read("$.length()");
		assertThat(length).isEqualTo(1);

		//IDS
		JSONArray ids = docContext.read("$..id");
		assertThat(ids).containsExactlyInAnyOrder(1);

		//NAME
		JSONArray names = docContext.read("$..name");
		assertThat(names).containsExactlyInAnyOrder("Jack");

		//AGE
		JSONArray ages = docContext.read("$..age");
		assertThat(ages).containsExactlyInAnyOrder(19);
	}

	@Test
	void shouldDeleteAgentById() {

	}

	@Test
	void shouldNotDeleteAgentByWrongId() {

	}

}
