
# Chapter 01: Application architecture

In this chapter we will focus on following activities:

1. Create application components diagram
1. Create API specifications for each backend service

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

### Work on authentication flow for applications

Since the beginning, our applications need to solve the authentication problem.
It means - user needs to authenticate in the frontend application somehow (same
for portal and user admin). It also means, that when frontend portal requests
some data from backend services - it needs to authenticate as user. Frontend
portal cannot simply request information from backend services as
unauthenticated user.

Let's keep the authentication flow very simple (see below image and
description):

![application-auth-flow](https://raw.githubusercontent.com/docent-net/golearnistio/main/chapter-01/learnistio-app-auth-flow.png)

1. When user authenticates in the frontend application by entering login and
   password
2. **frontend-portal** service sends POST request to **auth-service** to the
   /authorize endpoint
3. If credentials passed by user are fine, **auth-service** responds with a
   **session-token** that is saved in the memory of user browser by the
   **frontend-service**
4. Now, when user is authenticated, the **frontend-service** can display portal
   contents by fetching it from for instance **content-generator**
   /generate-endpoint This request is authenticated using HTTP authenticate
   header, that contains **session-token** provided by **frontend-service**
5. **content-generator** needs to verify, whether the request is legit by asking
   **auth-service** /verify-session-token endpoint if the session-token is fine
6. **auth-service** sends response with information regarding the correctness of
   the given session token. This is the moment when **content-generator**
   service makes decission whether it returns requested content to the
   **frontend-portal** or returns error
7. **content-generator** returns content (or error) to the **frontend-portal**

Above flow applies to all backend services (mailing-service and image-processor).

I decided to keep the authentication flow very simple in the beginning. So let's
assume, that:

1. **auth-service** will authenticate only user with following credentials:
    - login: user
    - password: user
1. **auth-service** will return session-token, that is a 32 - characters string
   ending with "5"
1. **auth-service** /verify-session-token endpoint verifies the session-token
   using only one rule: the end of the session-token string must be "5". So, we
   don't really verify here anything. That is because in the beginning we don't
   store session data in any database or cache (we will do it later)
1. In the [API specification](api-spec.md) all services' endpoints marked as
   **[auth required]** require session-token to be sent with the request as a
   subject of "Authorization: Bearer" header, e.g.:
   **Authorization: Bearer 32-chars-string-here**. This method of authorization
   is described in [RFC-6750](https://tools.ietf.org/html/rfc6750), but in our
   example we make it much simplier.
1. All those secured services' endpoints verify that session token by asking
   **auth-service** /verify-session-token endpoint if the token is correct or
   not.

**READ**:

nothing for now

**HOMEWORK**:

1. Create your own applications components diagram. Share it on [GH discussions](https://github.com/docent-net/golearnistio/discussions)
1. Create API specifications for your services. Share it on [GH discussions](https://github.com/docent-net/golearnistio/discussions)
1. Work on the authentication flow for your services. Share it on [GH discussions](https://github.com/docent-net/golearnistio/discussions)

**Recording**:

TBD