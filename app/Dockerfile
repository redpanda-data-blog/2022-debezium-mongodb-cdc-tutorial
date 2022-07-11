FROM python:3-alpine
USER root
RUN adduser -D muser
RUN pip install pymongo
ADD visited_classified_ads_gateway.py /home/muser
RUN chmod a+x /home/muser/visited_classified_ads_gateway.py
USER muser
ENTRYPOINT ["/home/muser/visited_classified_ads_gateway.py"]