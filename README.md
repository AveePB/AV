# Alien Intelligence Agency

## Table of contents
1. [Introduction](#introduction)
2. [Container Overview](#container_overview)
3. [Configuration Metadata](#configuration_metadata)
4. [Spring Annotations](#spring_annotations)
    - [@Configuration](#configuration_annotation)
    - [@Autowired](#autowired_annotation)
    - [@Component](#component_annotation)
    - [@Bean](#bean_annotation)
    - [@Service](#service_annotation)

## Introduction <a name="introduction"></a>
Welcome to the world of the "Alien Intelligence Agency," a fascinating Spring Boot project that delves into the intricate realm 
of basic bean annotations. Developed to unravel the fundamental concepts of Spring Boot and its powerful dependency injection 
mechanism, this project serves as an exploration into the core functionalities and uses of bean annotations.

## Container Overview <a name="container_overview"></a>
The ***org.springframework.context.ApplicationContext*** interface represents the **Spring IoC container** and is responsible 
for instantiating, configuring, and assembling the beans. The container gets its instructions on what objects 
to instantiate, configure, and assemble by reading configuration metadata. 

## Spring Configuration Files <a name="configuration_metadata"></a>
The configuration metadata is represented in **XML**, **Java annotations**, or **Java code**. It lets you express the objects that 
compose your application and the rich interdependencies between those objects.

## Spring Annotations <a name="spring_annotations"></a>
We can leverage the capabilities of Spring DI engine using the annotations in the ***org.springframework.beans.factory.annotation*** 
and ***org.springframework.context.annotation*** packages. We often call these **“Spring core annotations”**.

### @Configuration <a name="configuration_annotation"></a>
***@Configuration*** is a class-level annotation indicating that an object is a source of bean definitions. **@Configuration classes declare 
beans through @Bean-annotated methods**. Calls to ***@Bean*** methods on ***@Configuration*** classes can also be used to define inter-bean dependencies.

```
   @Configuration
   public class ManagerConfig {

       @Bean
       public AgentManager getAgentManager() {

           return new AgentManager();
       }
   
   }
```

This method of declaring inter-bean dependencies works only when the ***@Bean*** method is declared within a ***@Configuration*** class. 
**You cannot declare inter-bean dependencies by using plain @Component classes**.

### @Autowired <a name="autowired_annotation"></a>
The ***@Autowired*** annotation is performing **"Dependency Injection"**.

If ***@Autowired*** is applied to:
- a field: then the dependency is stored in this field.
- a setter: then the setter is invoked, with the parameter that is determined by the same algorithm as for the field dependency injection.
- a constructor: then the constructor is invoked with the parameters determined by the same algorithm as for the field dependency injection.  

```
   ...
```

### @Component <a name="component_annotation"></a>
Indicates that the annotated class is a component. Such classes are considered as candidates for auto-detection when using 
annotation-based configuration and classpath scanning.

```
   ...
```

### @Bean <a name="bean_annotation"></a>
To declare a bean, you can annotate a method with the ***@Bean*** annotation. You use this method to register a bean definition within 
an **ApplicationContext** of the type specified as the method’s return value. By default, **the bean name is the same as the method name**.

```
   ...
```

### @Service <a name="service_annotation"></a>
The ***@Service*** annotation is a specialization of the component annotation. It doesn’t currently provide any additional behavior over the ***@Component*** 
annotation, but it’s a good idea to use @Service over ***@Component*** in service-layer classes because it specifies intent better. 
Additionally, tool support and additional behavior might rely on it in the future.

```
   ...
```