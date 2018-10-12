//index.js
//获取应用实例
const app = getApp()

Page({
  data:{
    result: 0
  },
  changeNumber: function (e) {
    this.data.result += 1
    this.setData({
      result: this.data.result
    })
  },
  resetNumber:function(){
    this.setData({
      result:0
    })
  }

})

  



  
