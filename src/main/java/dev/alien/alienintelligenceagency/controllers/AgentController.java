package dev.alien.alienintelligenceagency.controllers;

import dev.alien.alienintelligenceagency.models.Agent;
import dev.alien.alienintelligenceagency.services.AgentService;

import dev.alien.alienintelligenceagency.services.MissionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.net.URI;
import java.util.List;


@RestController
@RequestMapping("/agent")
public class AgentController {

    @Autowired
    private MissionService missionService;

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

        this.missionService.removeAllMissionsByAgentId(id);
        this.agentService.removeAgentById(id);

        return ResponseEntity.noContent().build();
    }

}
