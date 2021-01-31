# golearnistio

Learn Istio by example and a bit of Golang!

<!-- TOC -->

- [golearnistio](#golearnistio)
        - [Chapters index](#chapters-index)
        - [What is it all about?](#what-is-it-all-about)
        - [How this works?](#how-this-works)
        - [A youtube stream](#a-youtube-stream)
        - [How long will it take?](#how-long-will-it-take)
        - [How to contact me?](#how-to-contact-me)

<!-- /TOC -->

### Chapters index

- [Chapter 00: High level plan](chapter-00/)
- Chapter 01: Application architecture
- Chapter 02: Implementing + installing application
- Chapter 03: Installing application w/Helmfile
- Chapter 04: Running application performance tests
- Chapter 05: Installing Istio
- Chapter 06: Istio: tracing
- Chapter 07: Istio: observability
- Chapter 08: Istio: gateway and SSL w/cert-manager
- Chapter 09: Istio: routing - basic traffic splitting
- Chapter 10: Istio: routing - advanced traffic splitting
- Chapter 11: Istio: routing - sticky sessions
- Chapter 12: Istio: routing - mirroring (dark traffic and live debugging)
- Chapter 13: Istio: fault injection
- Chapter 14: Istio: circuit breakers
- Chapter 15: Istio: JWT
- Chapter 16: Istio: mTLS
- Chapter 17: Istio: egress
- Chapter 18: Running application performance tests
- Chapter 19: Istio: multicluster setup

### What is it all about?

This is about you learning Istio. If you want of course. And story behind is.. I need an Istio crash course. A practical one, not theoretical.  Usually in that kind of situations I basically try installing, configuring and working with a service. However, in case of Istio you need a whole application in order to test Istio features.

I thought - I'm gonna create a plan of learning and share it with others. Usually, when I learn something, the next thing to do is a presentation on a meetup or a conference. However, this time I feel like needing more motivation, so I decided to go public and invite other to learn with me.

So, here we are :)

### How this works?

I'll post updates here (simply turn on watching custom events / pull requests for this repository) or [follow me on Twitter](https://twitter.com/docent_net) or [follow hastag #golearnistio](https://twitter.com/hashtag/golearnistio?src=hashtag_click)

Each "chapter" will specify a part that is to be **READ** by you (and ofc understand / process).

Also there will be a **HOMEWORK** part.

### A youtube stream

Beside notes, that are 100% enought to run this workshop yourself in your
lab, I'm running a youtube stream for each chapter. I'm basically recording
my work. The stream is available here: [golearnistio stream](https://www.youtube.com/watch?v=GgF6Ov5Pg80&list=PLe_xxswxhVz_XSGfhJq_oYtUgOgWoQu6Y&ab_channel=MaciejLasyk)

### How long will it take?

Whatever it needs. I'll probably post daily, so we move forward. But can't tell if it's one month or two when we finish.

### How to contact me?

The best way imo will be use [Github Discussions](https://github.com/docent-net/golearnistio/discussions). We're a community, thus we should help each other instead of funneling problems via just one person.

### Chapter 00: High - level plan

So I thought about it thoroughly and here's a plan, that we will follow (if you have some suggestions / ideas related to this plan - post it on [GH discussions](https://github.com/docent-net/golearnistio/discussions):

1. Appplication architecture
1. Installing application w/Helmfile
1. Running application performance tests
1. Installing Istio
1. Istio: tracing
1. Istio: observability
1. Istio: gateway and SSL w/cert-manager
1. Istio: routing - basic traffic splitting
1. Istio: routing - advanced traffic splitting
1. Istio: routing - sticky sessions
1. Istio: routing - mirroring (dark traffic and live debugging)
1. Istio: fault injection
1. Istio: circuit breakers
1. Istio: JWT
1. Istio: mTLS
1. Istio: egress
1. Running application performance tests
1. Istio: multicluster setup

**READ**:

- [Istio architecture](https://istio.io/latest/docs/ops/deployment/architecture/)
- [Istio deployment models](https://istio.io/latest/docs/ops/deployment/deployment-models/)
- [Helm package manager for k8s](https://helm.sh/docs/topics/charts/)
- [Helmfile for managing Helm charts](https://github.com/roboll/helmfile)

**HOMEWORK**:

1. Do you think above high-level plan is fine? Maybe you have any suggestions? Post it on [GH discussions](https://github.com/docent-net/golearnistio/discussions). Otherwise, you can always just say "hello" :)
1. You will need a K8S cluster (in last chapter even 2 clusters) for this workshop. It can be whatever cluster you have, but keep in mind, that K3S may not be enough (e.g. some problems w/installing Kiali on K3S: https://discuss.istio.io/t/jaeger-url-not-valid-in-kiali-configuration/5307/10). As for resources - we will use minimum number of resources. A couple of tiny services and that's all. We won't need any persistent storage. We'll redeploy applications quite often using Helmfile.
