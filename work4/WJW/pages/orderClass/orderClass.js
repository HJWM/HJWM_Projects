// pages/orderClass/orderClass.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    items: [
      { name: '主席团', value: '主席团',checked: 'true' },
      { name: '云计算', value: '云计算' },
      { name: '网媒组', value: '网媒组' },
      { name: '固宽组', value: '固宽组' },
      { name: '无线一', value: '无线一' },
      { name: '无线二', value: '无线二' },
      { name: '秘书处', value: '秘书处' },
      { name: '新媒体', value: '新媒体' },
    ],
    user:[],
    depart:"主席团",
    name:"张兴豪"
  },

  radioChange: function (e) {
    this.setData({
      depart: e.detail.value
    })
  },

  formSubmit: function(e){
    var user = this.data.user;
    var flag = false;
    var depart = this.data.depart;
    for(var num in user){
      if (e.detail.value.ordername === user[num].name){
        wx.navigateTo({
          url: '/pages/register/register?depart='+depart+'&'+'name='+user[num].name,
        }),
        flag = true;
      }
    }
    if(!flag){
      wx.navigateTo({
        url: '/pages/user/user',
      })
    }
   console.log(flag);
    //console.log('radio发生change事件，携带value值为：', e.detail.value.ordername)
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
    var that = this;
    that.setData({
      user: wx.getStorageSync("checckUser"),
    })
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