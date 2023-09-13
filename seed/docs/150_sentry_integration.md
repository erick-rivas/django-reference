## Sentry Integration ##

This file contains instructions to integrate Sentry with the project you are working on.

### Create project and get DNS

-   Go to the following URL: [https://sentry.io/auth/login]
-   Enter the correct credentials.
-   In the left menu, select the "Projects" option.
-   Create a new project with the necessary Framework and change the configuration as you need.


### Integrate support into the project

-   Request the dsn.
-   In the [Settings] file, change the dsn to the one indicated.
-   Change the parameters as you need:
    -   If you wish to associate users to errors (assuming you are using django.contrib.auth) you may enable sending PII data.
    -   Set traces_sample_rate to 1.0 to capture 100% of transactions for performance monitoring. It's recommend adjusting this value in production.