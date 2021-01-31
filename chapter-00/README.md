
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

**Recording**:

[![YouTube stream](http://i.imgur.com/Ot5DWAW.png)](https://www.youtube.com/embed/GgF6Ov5Pg80)