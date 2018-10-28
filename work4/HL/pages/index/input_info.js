// example/activity_room/input_info.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    date: '',
    begin_time: '',
    end_time: '',
    reason: '',
    name: '',
    department: '',
    uid: '',
    countryIndex: "0",
    countries: ["网媒", "新媒体", "云计算", "固宽", "无线一组", "无线二组", "秘书处", "主席团"],
    obj: {}
  },

  uidChange: function(e) {
    this.setData({
      uid: e.detail.value
    })
//    this.data.uid = e.detail.value
  },

  nameChange: function(e) {
    this.setData({
      name: e.detail.value
    })
//    this.data.name = e.detail.value
  },

  reasonChange: function(e) {
    this.setData({
      reason: e.detail.value
    })
//    this.data.reason = e.detail.value
  },

  bindCountryChange: function (e) {
    console.log('picker country 发生选择改变，携带值为', e.detail.value);
    this.setData({
      countryIndex: e.detail.value,
    })
  },

  bindDateChange: function (e) {
    console.log(e)
    this.setData({
      date: e.detail.value
    })
  },

  bindStartTimeChange: function (e) {
    this.setData({
      begin_time: e.detail.value
    })
  },

  bindEndTimeChange: function (e) {
    this.setData({
      end_time: e.detail.value
    })
  },

  submit_info: function(){
    this.setData({
      department: this.data.countries[this.data.countryIndex],
    })
    this.data.obj.uid = this.data.uid,
    this.data.obj.name = this.data.name,
    this.data.obj.department = this.data.department,
    this.data.obj.date = this.data.date,
    this.data.obj.begin_time = this.data.begin_time,
    this.data.obj.end_time = this.data.end_time,
    this.data.obj.reason = this.data.reason,
    console.log('组合成的对象',this.data.obj),
    wx.setStorage({
      key: 'user',
      data: this.data.obj,
      success: function() {
        wx.navigateBack();
      }
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