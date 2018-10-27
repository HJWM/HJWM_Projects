// pages/order/order.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    department:"...",
    name:"...",
    reasons: ["上自习", "学习交流", "活动排练","小组开会","其他"],
    reasonIndex: 0,
    orderdate: "2018-10-01",
    starttime: "9:00",
    endtime: "21:00",
    manyinfo:[]
  },
 


  bindDateChange: function (e) {
    this.setData({
      orderdate: e.detail.value
    })
  },
  bindTimeChange: function (e) {
    this.setData({
      starttime: e.detail.value
    })
  },
  bindendTimeChange: function (e) {
    this.setData({
      endtime: e.detail.value
    })
  },



  bindReasonChange: function (e) {
    console.log('picker  reason 发生选择改变，携带值为', e.detail.value);
    this.setData({
      reasonIndex: e.detail.value
    })
  },

  submitdate: function (event) {
    var reasonIndex = this.data.reasonIndex
    var reasons=this.data.reasons
    var someinfo = {
      "orderdate":this.data.orderdate,
      "starttime": this.data.starttime,
      "endtime": this.data.endtime,
      "reasons":reasons[reasonIndex],
      "department": this.data.department
      }

      var manyinfo=this.data.manyinfo;
      manyinfo.push(someinfo);
      wx.setStorage({
        key: 'manyinfo',
        data: manyinfo,
        success: function (res) {
          wx.navigateTo({
            url: '../result/result'
          })
          // console.log(manyinfo);
        }
      });
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var manyinfo = wx.getStorageSync('manyinfo');
    if (!manyinfo){
      this.setData({
        "manyinfo":[]
      })
    }else{
      this.setData({
        "manyinfo": manyinfo
      })
    }
   
    var mini = wx.getStorageSync('allinfo');
    console.log(mini)
    var department = mini[0].department;
    var name = mini[1].name;
    this.setData({
      "department": department,
      "name": name,
    })
    console.log(this.data.name);
    console.log(this.data.department);

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