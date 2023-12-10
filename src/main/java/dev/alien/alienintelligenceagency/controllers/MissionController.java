package dev.alien.alienintelligenceagency.controllers;

import dev.alien.alienintelligenceagency.models.Mission;
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
@RequestMapping("/mission")
public class MissionController {

    @Autowired
    private MissionService missionService;

    @Autowired
    private AgentService agentService;

    //CREATE:

    @PostMapping
    public ResponseEntity<String> createNewMission(@RequestBody Mission mission) {

        //Checks if agent with such id exists.
        if (this.agentService.fetchAgentById(mission.getAgentId()) == null)
            return ResponseEntity.unprocessableEntity().build();

        Mission createdMission = this.missionService.addNewMission(mission);

        URI resourceLocation = ServletUriComponentsBuilder.
                fromCurrentRequest().path("/{id}").
                buildAndExpand(createdMission.getId()).
                toUri();

        return ResponseEntity.created(resourceLocation).build();
    }

    //READ:

    @GetMapping("/{id}")
    public ResponseEntity<Mission> readMissionById(@PathVariable Long id) {

        Mission requestedMission = this.missionService.fetchMissionById(id);

        if (requestedMission == null)
            return ResponseEntity.notFound().build();

        return ResponseEntity.ok(requestedMission);
    }

    @GetMapping
    public ResponseEntity<List<Mission>> readAllMissions() {
        List<Mission> missions = this.missionService.fetchAllMissions();

        return ResponseEntity.ok(missions);
    }

    //UPDATE:

    @PutMapping("/{missionId}/{agentId}")
    public ResponseEntity<String> updateMissionAgentId(@PathVariable Long missionId, @PathVariable Long agentId) {

        //Checks if agent with such id exists.
        if (this.agentService.fetchAgentById(agentId) == null)
            return ResponseEntity.unprocessableEntity().build();


        Mission updatedMission = this.missionService.updateMissionAgentId(missionId, agentId);

        if (updatedMission == null)
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();

        return ResponseEntity.noContent().build();
    }

    //DELETE:

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteMissionById(@PathVariable Long id) {

        this.missionService.removeMissionById(id);

        return ResponseEntity.noContent().build();
    }

    @DeleteMapping("/all/{agentId}")
    public ResponseEntity<String> deleteAllMissionsByAgentId(@PathVariable Long agentId) {

        this.missionService.removeAllMissionsByAgentId(agentId);

        return ResponseEntity.noContent().build();
    }

}
