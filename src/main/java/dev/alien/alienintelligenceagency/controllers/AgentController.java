package dev.alien.alienintelligenceagency.controllers;

import dev.alien.alienintelligenceagency.models.Agent;
import dev.alien.alienintelligenceagency.services.AgentService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.net.URI;
import java.util.List;


@RestController
@RequestMapping("/agent")
public class AgentController {

    @Autowired
    private AgentService agentService;

    //CREATE:

    @PostMapping
    public ResponseEntity<String> createNewAgent(@RequestBody Agent agent) {

        Agent createdAgent = this.agentService.addNewAgent(agent);

        URI resourceLocation = ServletUriComponentsBuilder.
                fromCurrentRequest().path("/{id}").
                buildAndExpand(createdAgent.getId())
                .toUri();

        return ResponseEntity.created(resourceLocation).build();
    }

    //READ:

    @GetMapping("/ask/{id}")
    public ResponseEntity<Boolean> containsAgentWithId(@PathVariable Long id) {

        Boolean answer = this.agentService.containsAgentWithId(id);

        return ResponseEntity.ok(answer);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Agent> readAgentById(@PathVariable Long id) {

        Agent requestedAgent = this.agentService.fetchAgentById(id);

        if (requestedAgent == null)
            return ResponseEntity.notFound().build();

        return ResponseEntity.ok(requestedAgent);
    }

    @GetMapping
    public ResponseEntity<List<Agent>> readAllAgents() {

        List<Agent> agents = this.agentService.fetchAllAgents();

        return ResponseEntity.ok(agents);
    }

    //DELETE:

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteAgentById(@PathVariable Long id) {

        //DELETE ALL MISSIONS WITH THIS AGENT's ID...

        this.agentService.removeAgentById(id);

        return ResponseEntity.noContent().build();
    }

}
