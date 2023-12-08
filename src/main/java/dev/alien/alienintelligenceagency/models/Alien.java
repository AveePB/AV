package dev.alien.alienintelligenceagency.models;

import dev.alien.alienintelligenceagency.enums.JobType;

import jakarta.persistence.Column;
import jakarta.persistence.Enumerated;
import jakarta.persistence.EnumType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import java.util.Objects;


@Entity
@Table(name = "aliens")
public class Alien {

    @Id
    @GeneratedValue
    private Long id;

    @Column(name = "job_type", nullable = false)
    @Enumerated(value = EnumType.STRING)
    private JobType jobType;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "age", nullable = false)
    private Integer age;


    public Alien(Long id, JobType jobType, String name, Integer age) {
        this.id = id;
        this.jobType = jobType;
        this.name = name;
        this.age = age;
    }

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public JobType getJobType() {
        return this.jobType;
    }

    public void setJobType(JobType jobType) {
        this.jobType = jobType;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return this.age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Alien alien = (Alien) o;
        return Objects.equals(this.id, alien.id) && this.jobType == alien.jobType && Objects.equals(this.name, alien.name) && Objects.equals(this.age, alien.age);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id, this.jobType, this.name, this.age);
    }

    @Override
    public String toString() {
        return "Alien{" +
                "id=" + this.id +
                ", jobType=" + this.jobType +
                ", name='" + this.name + '\'' +
                ", age=" + this.age +
                '}';
    }

}
