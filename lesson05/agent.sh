curl -sO http://localhost:8080/jnlpJars/agent.jar
java -jar agent.jar -jnlpUrl http://localhost:8080/computer/local/jenkins-agent.jnlp -secret 9fe51de34ee74e43ef0080ba5a580ebd0174fc405e5563718b3dc07e9dbdba8b -workDir "/tmp"