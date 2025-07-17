#CRM TOPIC
from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})


topic_list = []
topic_list.append(NewTopic(topic="crm_events", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
print('done')

#ERP TOPIC
from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})


topic_list = []
topic_list.append(NewTopic(topic="erp_events", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)


print('done')

#APP Topic 

from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})


topic_list = []
topic_list.append(NewTopic(topic="app_events", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

print('done')


#WEBSITE TOPIC

from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})


topic_list = []
topic_list.append(NewTopic(topic="website_events", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

print('done')