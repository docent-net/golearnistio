
# Chapter 02: Implementing application

This will be a coding session.

If you have programming experience, than simply do it yourself and remember to work on your own application architecture and API specifications (all those things were a subject of previous [Chapter 01](../chapter-01/README.md)).

If you aren't fluent w/coding, or just don't have time - you can simply use the code, that I will create during this chapter.

I'll be using application architecture created in [Chapter 1](../chapter-01/README.md), so basically this:

![application-components](https://raw.githubusercontent.com/docent-net/golearnistio/main/chapter-01/application-components.png)

And the [API specification is here](../chapter-01/api-spec.md).

### Containerize applications

When application services are ready, we're gonna containerize those. I'll be using fedora-minimal images from [registry.fedoraproject.org/](https://registry.fedoraproject.org/) and Dockerfile format. You can of course use any kind of image (but plz, don't use Alpine, I elaborated about it [during OWASP meeting a few years ago](https://maciej.lasyk.info/slides/OWASP_more_about_linux_containers.pdf)).

Also, my homelab K8S clusters run Docker inside, but no problem with having CRI-O or any other container engine.

**READ**:

nothing for now

**HOMEWORK**:

1. Implement your application services; make them connect to DBs (but we don't have DBs yet, so basically timeout connections and return errors defined in API spec; yes, we expose/leak errors to API clients - this is just a workshop)
1. Containerize those services using any kind of container technology you use on your Kubernetes cluster

**Recording**:

TBD