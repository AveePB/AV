package dev.alien.alienintelligenceagency.repos;

import dev.alien.alienintelligenceagency.models.Mission;

import jakarta.transaction.Transactional;
import org.springframework.data.jpa.repository.JpaRepository;


public interface MissionRepository extends JpaRepository<Mission, Long> {

    //CREATE

    //READ

    //UPDATE

    //DELETE
    @Transactional
    void deleteAllByAgentId(Long agentId);
}
