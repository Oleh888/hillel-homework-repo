# Build the application jar
FROM maven:3.8.4-openjdk-17 AS builder

COPY application/pom.xml /
COPY application/src/ /src/

RUN mvn -DappJarName=demo-app package

# Build the application runtime image
FROM eclipse-temurin:17.0.8_7-jre

COPY --from=builder /target/demo-app.jar /

ENTRYPOINT ["sh", "-c", "java -jar demo-app.jar"]
