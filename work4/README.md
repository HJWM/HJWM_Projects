# 小程序开发实战：活动室预约

### 一、开发内容

实现“西电华小为”小程序的活动室预约功能，不需要考虑与后端交互。当前的活动室预约的产品逻辑为：

- 打开首页，加载已预约的信息，查询当前用户
  - 浏览首页，点击每个预约信息，可弹出Toast查看预约人和预约理由
  - 点击新增按钮
    - 若当前用户为注册，进入注册页面，填写姓名部门，成功后返回首页
    - 若当前用户已注册，进入预约页面，可选择日期、开始时间、结束时间、预约原因，进行预约，成功后返回首页

### 二、开发要点

1. 首页每次显示的时候都要重新刷新预约信息和用户

2. 新注册用户可暂存到LocalStorage中，供鉴别用户是否注册

3. 每一条用户信息包含：日期、开始时间、结束时间、预约原因、用户名、用户部门、用户uid（uid自己随便指定一个就行）

4. 注意 JS 模块化，将预约信息（加载已有、新增）、用户信息（注册、查询）均可封装到utils目录下，模拟真实开发场景下的 HTTP 请求

5. 有能力的同学可考虑使用 weui.wxss 完成本次作业，此 UI 库的使用比较简单，建议自学，后期不做单独讲解。

### 三、参考链接

1. 官方文档 - [框架](https://developers.weixin.qq.com/miniprogram/dev/framework/MINA.html)、[组件](https://developers.weixin.qq.com/miniprogram/dev/component/)、[API](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html)

2. [微信小程序-调用工具js文件/utils文件中的函数/变量](https://www.cnblogs.com/bellagao/p/6305485.html)

3. [weui.wxss](https://github.com/Tencent/weui-wxss)

