// pages/user/user.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    obj:{},
    arr:[],
    disabled:false,
  },

  userNum:function(e){
    let m = this.data.obj;
    m.name = e.detail.value.name;
    m.sort = e.detail.value.sort;
    var arr = wx.getStorageSync('checckUser');
    arr.push(m);
    wx.setStorageSync('checckUser',arr);
    wx.redirectTo({
      url: '/pages/index/index',
    })
  },

  disableButton:function(){
    this.setData({
      disabled : true
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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