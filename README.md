# Mockup for IoT communications

## Raspberry pi mock 

The raspberry pi listens to the GET requests from the IoT device.  Fire up the flask server: 
```
python pi_flask.py
```

Make sure the server is alive:
```
http://localhost:8001/hello
```

Now, pretend you are an IoT device by opening a url like this one in Chrome:
```
http://localhost:8001/position?position=1.23&comment=ElleKnowsPython
```

This echos your data in the browser and does some other magic.  After you do make a couple 
you should see the log file filing up:
```
(root) λ tail -f _position.txt
2019-11-06 19:52:07.269815, 27, Shop smart, shop s-mart
2019-11-06 19:52:09.577642, 28, Shop smart, shop s-mart
2019-11-06 19:52:11.887463, 29, Shop smart, shop s-mart
2019-11-06 19:52:14.196287, 30, Shop smart, shop s-mart
2019-11-06 19:52:16.511096, 31, Shop smart, shop s-mart
2019-11-06 19:52:18.819919, 32, Shop smart, shop s-mart
2019-11-06 19:52:21.134727, 33, Shop smart, shop s-mart
2019-11-06 19:52:23.450533, 34, Shop smart, shop s-mart
2019-11-06 19:52:25.760354, 35, Shop smart, shop s-mart
2019-11-06 19:54:09.549980, 1, foo
```

## Mock the IoT device

Since we are lazy we can make a small script to pretend like it's a IoT device
and send random data to the flask server on an interval.

```
python mock_io_position.py
```

## What's next

  1. Keep the flask server running on a PC/Raspberry pi. 
  2. Setup the IoT device to send data to the PC/Raspbery pi.
  3. Watch the PC/Raspberry pi terminal as the data comes in.
  4. ...
  5. Profit

