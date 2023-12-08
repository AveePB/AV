package dev.alien.alienintelligenceagency.models;

import dev.alien.alienintelligenceagency.enums.MissionType;

import jakarta.persistence.Column;
import jakarta.persistence.Enumerated;
import jakarta.persistence.EnumType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import java.util.Objects;


@Entity
@Table(name = "missions")
public class Mission {

    @Id
    @GeneratedValue
    private Long id;

    @Column(name = "mission_type", nullable = false)
    @Enumerated(value = EnumType.STRING)
    private MissionType missionType;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "agent_id", nullable = false)
    private Long agentId;


    public Mission(Long id, MissionType missionType, String name, Long agentId) {
        this.id = id;
        this.missionType = missionType;
        this.name = name;
        this.agentId = agentId;
    }

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public MissionType getMissionType() {
        return this.missionType;
    }

    public void setMissionType(MissionType missionType) {
        this.missionType = missionType;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Long getAgentId() {
        return this.agentId;
    }

    public void setAgentId(Long agentId) {
        this.agentId = agentId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Mission mission = (Mission) o;
        return Objects.equals(this.id, mission.id) && this.missionType == mission.missionType && Objects.equals(this.name, mission.name) && Objects.equals(this.agentId, mission.agentId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id, this.missionType, this.name, this.agentId);
    }

    @Override
    public String toString() {
        return "Mission{" +
                "id=" + this.id +
                ", missionType=" + this.missionType +
                ", name='" + this.name + '\'' +
                ", agentId=" + this.agentId +
                '}';
    }

}
