chaplus_ros
===========

ROS package for https://www.chaplus.jp/

## Tutorials

1) Obtain API keys for chaplus service, goto https://www.chaplus.jp/api and send an e-mail, then you can get your API key in the e-mail.

2) Put API key as json file under `` `rospack find chaplus_ros`/apikey.json ``
   ```
   {"apikey": "0123456789"}
   ```

## Interface

### Subscribing Topics

- request (std_msgs/String)

  Input text data for chaplus bot system.

### Publishing Topics

- response (std_msgs/String)

  Response text data from chaplus bot system.

### Parameters

- ~chaplus_apikey_file (String: default: `rospack find chaplus_ros`/apikey.json

  Path to json file stores chaplus API key.

Sample Code
-----------

1) sample/julius_example.launch

Example to listen from your mic and respond from speakers, This demo uses Julius for speech to text engine, which requires vocabulary list. You need to change following line of the `julius_example.launch` to let system recognize your talk. Note that julius needs 20-30 seconds to update it's vocabulary list, so please be patient after you send the list from your command line.
```
  <!-- julius needs vocabulary list -->
  <node pkg="rosservice" type="rosservice" name="update_vocabulary_list"
        args='call --wait /speech_recognition "{vocabulary: {words: ["こんにちは", "おはよう"]}}"' />
```

2) sample/google_example.launch

Example with google speech recognition. This demo requires [google_cloud_credentials_json](https://github.com/jsk-ros-pkg/jsk_3rdparty/tree/master/ros_speech_recognition#parameters), and update following line of the `google_example.launch`
```
  <param name="/speech_recognition/google_cloud_credentials_json"
         value="/home/k-okada/Downloads/eternal-byte-236613-4bc6962824d1.json" />
```
