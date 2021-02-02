
# Chapter 01: Appplication architecture

In this chapter we will focus on couple of activities:

1. Create application components diagram
1. Create API specifications for each backend service
1. Implement applications one-by-one
1. Containerize applications

### Create application components diagram

First things first. We need to create an application architecture diagram,
which will help us understand how services connect to each other.

Classical web application would consist of:

1. Frontend components: portal (e.g. the main webpage), administration
panel (where administrator commit some administrative tasks)
1. Backend components: all those services that process data, serves API
endpoints to frontend and talk to databases, queues and caches
1. Databases, queues, caches etc

I came out with something like this:

![application-components](https://raw.githubusercontent.com/docent-net/golearnistio/main/chapter-01/application-components.png)

Work out your own. Seriously. Even on sheet of paper. I use
[LucidCharts](https://lucid.app/) for creating those kind of diagrams, but it
really doesn't matter - use whatever tool you have.

Go through list of this workshop chapters and think about possible scenarios
that we will test (regarding Istio configurations). This should help you draw
those arrows between services.

### Create API specifications for each backend service

Most backend services will provide some API endpoints that will be used for
exchanging data between components. Later we will blow up some of those
connection lines (playing with various Istio configurations). That's why we
need to document how our APIs work and also include some maintenance endpoints
that will tell us the state of the service itself as well as connectivity from
this service to other services.

I created [API specification here](api-spec.md). In order to do that I took a
look at components diagram and noted whether particular component connects to
DBs or not as well as whether it connects to other backend services. This way
I created some endpoints that will help me diagnose the state of each service
and its connection to other services.

Also, each service provides some endpoints specifi to that service. Those will
be rather bogus-endpoints, that does almost nothing (almost, because it will
e.g. try to connect to database or queue and maybe even fetch some data - we
will see).

### Implement applications one-by-one

TBD

### Containerize applications

TBD

**READ**:

nothing for now

**HOMEWORK**:

1. Create your own applications components diagram. Share it on [GH discussions](https://github.com/docent-net/golearnistio/discussions)
1. Create API specifications for your services. Share it on [GH discussions](https://github.com/docent-net/golearnistio/discussions)

**Recording**:

TBD, probably will record this in couple of shorter sessions