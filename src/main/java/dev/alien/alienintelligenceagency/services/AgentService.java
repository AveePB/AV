package dev.alien.alienintelligenceagency.services;

import dev.alien.alienintelligenceagency.models.Agent;
import dev.alien.alienintelligenceagency.repos.AgentRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;


@Service
public class AgentService {

    private AgentRepository agentRepository;

    @Autowired
    public AgentService(AgentRepository agentRepository) {
        this.agentRepository = agentRepository;
    }

    //CREATE:

    public Agent addNewAgent(Agent agent) {
        agent.setId(null);

        return this.agentRepository.save(agent);
    }

    //READ:

    public boolean containsAgentWithId(Long id) {
        Optional<Agent> optionalAgent = this.agentRepository.findById(id);

        return optionalAgent.isPresent();
    }

    public Agent fetchAgentById(Long id) {
        Optional<Agent> optionalAgent = this.agentRepository.findById(id);

        if (optionalAgent.isEmpty())
            return null;

        return optionalAgent.get();
    }

    public List<Agent> fetchAllAgents() {
        return this.agentRepository.findAll();
    }


    //DELETE:

    public void removeAgentById(Long id) {

        this.agentRepository.deleteById(id);
    }

}
