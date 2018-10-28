// pages/register/register.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    obj:{},
    depart:"",
    name:""
  },

  registerNum: function(e){
    let m= this.data.obj;
    m.depart = this.data.depart;
    m.username = this.data.name;
    m.time = e.detail.value.time;
    m.start = e.detail.value.start;
    m.end = e.detail.value.end;
    m.reason = e.detail.value.reason;
    this.setData({
      obj: m
    })
    app.globalData.orderInfo.push(m);
    wx.redirectTo({
      url: '/pages/index/index',
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      depart:options.depart,
      name:options.name
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