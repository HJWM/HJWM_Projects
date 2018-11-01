//pages/result/result.js
//获取应用实例
const app = getApp()

Page({
  data:{
    reserveInfo:[]
  },
  /*回调函数，需要进一步了解
  bindtoReserve: function (e) {
    let userInfo = wx.getStorage({
      key: "userInfo",
      success: function (res) {  //再执行这个
        console.log(res.data);
        return(res.data);
      }
    });
    console.log(userInfo); //先执行这个
  }*/  
  onLoad: function(e){
    var that = this;
    let reserveInfo = this.data.reserveInfo;
    wx.getStorage({
      key: "reserveInfo",
      success: function (res) {
        //console.log(res.data);
        that.setData({
          reserveInfo: res.data
        })
      }
    })
  },
  showReason: function (e) {
    let name = e.target.dataset.name;
    let reason = e.target.dataset.reason;
    wx.showToast({
        title: name + "：" + reason,
        icon: "none",
    })
  },
  bindtoReserve: function (e) {
    wx.getStorage({
      key: "userInfo",
      success: function (res) {
        wx.navigateTo({
         url: "../reserve/reserve"
        })
      },
      fail: function (res) {
        wx.navigateTo({
          url: "../login/login"
        })
      }
    });
  }
})