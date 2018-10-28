// pages/showInfo/showInfo.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    arr:[],
    src: '../../public/imag/add.png',
    mode:"aspectFill",
    size:"mini",
    depart:"",
  },
  showok:function(event){
    var time = event.currentTarget.dataset.time;
    var depart = event.currentTarget.dataset.depart;
    wx.showToast({
      title: "日期是"+':'+time+"部门:"+depart,
      icon:'none',
      duration: 2000
    })  
  }
,
loadInfo:function(){
  let arr = wx.getStorageSync("checckUser");
  if(!arr){
    wx.setStorageSync("checckUser", app.globalData.userInfo);
  }
  
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    this.setData({
      arr:app.globalData.orderInfo,
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})