//pages/index/index.js
//获取应用实例
const app = getApp()

Page({
  //事件处理函数
  bindTaptoReservation: function() {
    //wx.getStorage({
    // key: "revInfo",
    //  success: function(res) {console.log(res.data)}
    //})
    wx.navigateTo({
      url: "../result/result"
    })
  }
})
