package dev.alien.alienintelligenceagency.services;

import dev.alien.alienintelligenceagency.models.Mission;
import dev.alien.alienintelligenceagency.repos.MissionRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;


@Service
public class MissionService {

    private MissionRepository missionRepository;

    @Autowired
    public MissionService(MissionRepository missionRepository) {
        this.missionRepository = missionRepository;
    }

    //CREATE:

    public Mission addNewMission(Mission mission) {
        mission.setId(null);

        //MISSION AGENT_ID CHECK...

        return this.missionRepository.save(mission);
    }

    //READ:

    public Mission fetchMissionById(Long id) {
        Optional<Mission> optionalMission = this.missionRepository.findById(id);

        if (optionalMission.isEmpty())
            return null;

        return optionalMission.get();
    }

    public List<Mission> fetchAllMissions() {

        return this.missionRepository.findAll();
    }

    //UPDATE:

    public Mission updateMissionAgentIdById(Long id, Long newAgentId) {

        //MISSION AGENT_ID CHECK...

        Optional<Mission> optionalUpdatedMission = this.missionRepository.findById(id);

        if (optionalUpdatedMission.isEmpty())
            return null;

        Mission updatedMission = optionalUpdatedMission.get();
        updatedMission.setAgentId(newAgentId);

        return this.missionRepository.save(updatedMission);
    }


    //DELETE:

    public void removeMissionById(Long id) {

        this.missionRepository.deleteById(id);
    }

    public void removeAllMissionsByAgentId(Long agentId) {

        this.missionRepository.deleteAllByAgentId(agentId);
    }

}
