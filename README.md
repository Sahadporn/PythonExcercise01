# Python practice with rabbitmq

## Steps

- [X] Install pyenv
- [X] Use python version 3.8
- [X] ทำ publisher ( Rabbitmq )
- [X] ส่งข้อมูล Ex. {“_id”: “5630252488”, “name”: “pipusana petgumpoom”, “age”: 27, created_at: ...(lib arrow) (utc datetime), updated_at: ... (utc datetime)}
- [X] ทำ consumer รับข้อมูล ( Rabbitmq )
- [ ] ถ้าเป็นข้อมูล นิสิตใหม่ให้ save ลงถังข้อมูลได้เลย  (Mongodb)
- [ ] ถ้าเป็นข้อมูลของ นิสิตเก่าให้ทำงาน check การเปลี่ยนแปลงของข้อมูล (Redis )แล้วทำการ Update ข้อมูลที่เปลี่ยนแปลงลงไป  (Mongodb)
