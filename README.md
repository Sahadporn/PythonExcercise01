# Python practice with rabbitmq

## Steps

- [X] Install pyenv
- [X] Use python version 3.8
- [X] ทำ publisher ( Rabbitmq )
- [X] ส่งข้อมูล Ex. {“_id”: “5630252488”, “name”: “pipusana petgumpoom”, “age”: 27, created_at: ...(lib arrow) (utc datetime), updated_at: ... (utc datetime)}
- [X] ทำ consumer รับข้อมูล ( Rabbitmq )
- [X] ถ้าเป็นข้อมูล นิสิตใหม่ให้ save ลงถังข้อมูลได้เลย  (Mongodb)
- [X] ถ้าเป็นข้อมูลของ นิสิตเก่าให้ทำงาน check การเปลี่ยนแปลงของข้อมูล (Redis )แล้วทำการ Update ข้อมูลที่เปลี่ยนแปลงลงไป  (Mongodb)

## Test

| | |
|---| --- |
| Send data for the first time | Pass |
| Update data | Pass |
| Send data to 2 consumer of the same type | Fail: DuplicateKeyError: E11000 duplicate key error (Some time error sometime success). Tried using session transaction but failed. |
| Publish data when there are no comsumer | Pass |
