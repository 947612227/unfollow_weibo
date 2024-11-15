# unfollow_weibo
批量取消微博关注


# 食用方法
1.打开微博网页端，点击登录，扫码（账号密码也行）登录即可
2.登录成功按下F12，或者右键选择开发者工具，刷新页面
3.随便选择一个接口，不是红色的即可，右键复制cookie 到代码headers中 对应位置
![微博复制这一块放到代码里面](https://github.com/user-attachments/assets/685d22d4-1b79-4a49-80ae-068177cdb3b6)
4.然后去关注列表中随便找个路人点击取消关注
![image](https://github.com/user-attachments/assets/fe8fe1e3-5ba6-454f-b8c7-696ccf5a9780)
然后复制 uid 填写到代码中对应位置
5.终端执行命令
```python
python3 微博取消关注.py
```
