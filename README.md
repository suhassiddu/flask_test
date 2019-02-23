# Flask Rest Api Test

Hosted on [https://suhasflask.herokuapp.com/](https://suhasflask.herokuapp.com/)

# Check with Curl
```
$ curl https://suhasflask.herokuapp.com/ifsc/<string:ifsc_code>

Example:

$ curl  https://suhasflask.herokuapp.com/ifsc/abhy0065004 | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   206  100   206    0     0    113      0  0:00:01  0:00:01 --:--:--   113
{
  "branch": "BHANDUP",
  "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
  "city": "MUMBAI",
  "district": "GREATER MUMBAI",
  "state": "MAHARASHTRA",
  "name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
}

$ curl  -H 'Content-Type: application/json' -H 'Accept: application/json' https://suhasflask.herokuapp.com/banks/ -X PUT -d '{"name": <string:bank_name>, "city": <string:city_name>}'

$ curl  -H 'Content-Type: application/json' -H 'Accept: application/json' https://suhasflask.herokuapp.com/banks/ -X PUT -d '{"name": "hdfc bank", "city": "mumbai"}' | jq . | head
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 39515  100 39476  100    39  18446     18  0:00:02  0:00:02 --:--:-- 18464
[
  {
    "ifsc": "HDFC0000001",
    "branch": "TULSIANI CHMBRS - NARIMAN PT",
    "address": "101-104 TULSIANI CHAMBERSFREE PRESS JOURNAL MARGNARIMAN POINTMUMBAIMAHARASHTRA400 021",
    "district": "GREATER MUMBAI",
    "state": "MAHARASHTRA"
  },
  {
    "ifsc": "HDFC0000002",
```
