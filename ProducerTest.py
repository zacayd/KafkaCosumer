from kafka import KafkaProducer

import time

# Topics/Brokers
topic1 = 'kafka-tst-04'
brokers = ['192.168.100.11:9092']


producer = KafkaProducer(bootstrap_servers=brokers)

# The send() method creates the topic
x = range(1000)
for n in x:
  print(n)
  print("Hello World!")
  producer.send(topic1, value=bytes(str(n), 'utf-8'))
  producer.flush()
  time.sleep(3)

# # One more example
# producer.send(topic1, key=b'event#2', value=b'This is a Kafka-Python basic tutorial')
# producer.flush()