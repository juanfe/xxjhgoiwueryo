/* ************************************************************************

#asset(qx/icon/${qx.icontheme}/16/actions/dialog-ok.png)
#asset(qx/icon/${qx.icontheme}/16/actions/dialog-cancel.png)

************************************************************************ */

qx.Class.define("web.Control",
{
  extend : qx.ui.window.Window,

  events : {
	      "changeData" : "qx.event.type.Data"
  },

  construct : function()
  {
    this.base(arguments, "");
    this.setShowMaximize(false);
    this.setShowMinimize(false);
    this.setWidth(950);
    this.setHeight(150);
    this.setShowClose(false);

    this.CtlLayout = new qx.ui.layout.Grid(10, 20);
	this.setLayout(this.CtlLayout);

    var toolbar = new qx.ui.toolbar.ToolBar();
    this.add(toolbar, {row: 0, column: 0, colSpan: 7});

    var TBPart1 = new qx.ui.toolbar.Part();

    //TODO add icons
    //var BtnPlaceBids = new qx.ui.toolbar.Button("Find My Assets", "icon/22/actions/document-new.png");
    var BtnPlaceBids = new qx.ui.toolbar.Button("Find My Assets");

    var BtnHome = new qx.ui.toolbar.Button("Return to My Spot");
    TBPart1.add(BtnPlaceBids);
    TBPart1.add(BtnHome);
    TBPart1.add(new qx.ui.toolbar.Separator());
    toolbar.add(TBPart1);

    var TBPart2 = new qx.ui.toolbar.Part();
    var BtnLogout = new qx.ui.toolbar.Button("Logout");
    TBPart2.add(BtnLogout);
    toolbar.add(TBPart2);

    toolbar.addSpacer();

    //var helpButton = new qx.ui.toolbar.Button("Help", "icon/22/actions/help-contents.png");
    var helpButton = new qx.ui.toolbar.Button("Help");
    toolbar.add(helpButton);

    this.setContentPadding(0);

    // Date Field Control
    var format2 = new qx.util.format.DateFormat("MM/dd/yyyy");
    var dateFieldFormat = new qx.ui.form.DateField();
    dateFieldFormat.setDateFormat(format2);
	
	var lblCorLogFraudRiskScore = new qx.ui.basic.Label();
	lblCorLogFraudRiskScore.setValue("CoreLogic Fraud Risk Score");
	this.add(lblCorLogFraudRiskScore, {row: 1, column: 0, rowSpan: 0});

	var lblCorLogCollRiskScore = new qx.ui.basic.Label();
	lblCorLogCollRiskScore.setValue("CoreLogic Collateral Risk Score");
	this.add(lblCorLogCollRiskScore, {row: 2, column: 0, rowSpan: 0}); 

	var lblMinLoanAmount = new qx.ui.basic.Label();
	lblMinLoanAmount.setValue("Loan Amount (minimum)");
	this.add(lblMinLoanAmount, {row: 3, column: 0, rowSpan: 0}); 

	var lblMaxLoanAmount = new qx.ui.basic.Label();
	lblMaxLoanAmount.setValue("Loan Amount (maximum)");
	this.add(lblMaxLoanAmount, {row: 4, column: 0, rowSpan: 0}); 

	var lblLienType = new qx.ui.basic.Label();
	lblLienType.setValue("Lien Type");
	this.add(lblLienType, {row: 1, column: 2, rowSpan: 0});

	var lblMaxLoanToValue = new qx.ui.basic.Label();
	lblMaxLoanToValue.setValue("Max LTV");
	this.add(lblMaxLoanToValue, {row: 2, column: 2, rowSpan: 0});
        this.AddPopup ("Maximun Loan To Value", lblMaxLoanToValue);

	var lblMaxComLoanToValue = new qx.ui.basic.Label();
	lblMaxComLoanToValue.setValue("Max CLTV");
	this.add(lblMaxComLoanToValue, {row: 3, column: 2, rowSpan: 0});
        this.AddPopup ("Maximun Combined Loan To Value", lblMaxComLoanToValue);

	var lblLoanType = new qx.ui.basic.Label();
	lblLoanType.setValue("Loan Type");
	this.add(lblLoanType, {row: 4, column: 2, rowSpan: 0});

	var lblMaxAdvance = new qx.ui.basic.Label();
	lblMaxAdvance.setValue("Max advance %");
	this.add(lblMaxAdvance, {row: 1, column: 4, rowSpan: 0});

	var lblAcceptableFICO = new qx.ui.basic.Label();
	lblAcceptableFICO.setValue("Acceptable FICO range");
	this.add(lblAcceptableFICO, {row: 2, column: 4, rowSpan: 0});

	var lblPropertyType = new qx.ui.basic.Label();
	lblPropertyType.setValue("Property Type");
	this.add(lblPropertyType, {row: 3, column: 4, rowSpan: 0});

	var lblAcceptState = new qx.ui.basic.Label();
	lblAcceptState.setValue("Acceptable State of property");
	this.add(lblAcceptState, {row: 5, column: 0, rowSpan: 0});

    this.SLCorLogFraudRiskScore = new qx.ui.form.Slider().set({
		minimum: 0,
        maximum: 1000,
        value: 1000,
		singleStep: 1,
		pageStep: 100
    });
    this.add(this.SLCorLogFraudRiskScore, {row: 1, column: 1, rowSpan:0});

    this.SLCorLogCollRiskScore = new qx.ui.form.Slider().set({
		minimum: 0,
        maximum: 1000,
        value: 1000,
		singleStep: 1,
		pageStep: 100
    });
    this.add(this.SLCorLogCollRiskScore, {row: 2, column: 1, rowSpan:0});
	
    this.SLAcceptableFICO = new qx.ui.form.Slider().set({
		minimum: 0,
        maximum: 550,
        value: 550,
		singleStep: 1,
		pageStep: 50
    });
    this.add(this.SLAcceptableFICO, {row: 2, column: 5, rowSpan:0, colSpan:2});

    // Number format Test
    var nfmoney = new qx.util.format.NumberFormat();
    nfmoney.setMinimumFractionDigits(2);
    nfmoney.setMaximumFractionDigits(2);

    var nfpercent = new qx.util.format.NumberFormat();
    nfpercent.setMinimumFractionDigits(1);
    nfpercent.setMaximumFractionDigits(2);

    //TODO read the maximum value of the column P Loan Amount and set the min and maximun value
    this.SPMinLoanAmount = new qx.ui.form.Spinner(0, 0, 1250000);	
    this.SPMinLoanAmount.setHeight(20);
    this.SPMinLoanAmount.setSingleStep(1000);
    this.SPMinLoanAmount.setWidth(100);
    this.SPMinLoanAmount.setNumberFormat(nfmoney);

    this.SPMaxLoanAmount = new qx.ui.form.Spinner(0, 1250000, 1250000);	
    this.SPMaxLoanAmount.setHeight(20);
    this.SPMaxLoanAmount.setSingleStep(1000);
    this.SPMaxLoanAmount.setWidth(100);
    this.SPMaxLoanAmount.setNumberFormat(nfmoney);

    this.SPMaxLoanToValue = new qx.ui.form.Spinner(0, 100, 100);	
    this.SPMaxLoanToValue.setSingleStep(1);
    this.SPMaxLoanToValue.setWidth(100);
    this.SPMaxLoanToValue.setNumberFormat(nfmoney);
    this.AddPopup ("Maximun Loan To Value", this.SPMaxLoanToValue);

    this.SPMaxComLoanToValue = new qx.ui.form.Spinner(0, 100, 100);	
    this.SPMaxComLoanToValue.setSingleStep(1);
    this.SPMaxComLoanToValue.setWidth(100);
    this.SPMaxComLoanToValue.setNumberFormat(nfpercent);
    this.AddPopup ("Maximun Combined Loan To Value", this.SPMaxComLoanToValue);

    this.SPMaxAdvance = new qx.ui.form.Spinner(0, 100, 100);	
    this.SPMaxAdvance.setSingleStep(1);
    this.SPMaxAdvance.setWidth(100);
    this.SPMaxAdvance.setNumberFormat(nfpercent);

    this.add(this.SPMinLoanAmount, {row: 3, column: 1, rowSpan:0});
    this.add(this.SPMaxLoanAmount, {row: 4, column: 1, rowSpan:0});
    this.add(this.SPMaxLoanToValue, {row: 2, column: 3, rowSpan:0});
    this.add(this.SPMaxComLoanToValue, {row: 3, column: 3, rowSpan:0});
    this.add(this.SPMaxAdvance, {row: 1, column: 5, rowSpan:0, colSpan:2});

    this.CBLienType = new qx.ui.form.ComboBox();
    this.CBLienType.add(new qx.ui.form.ListItem("First"));
    this.CBLienType.add(new qx.ui.form.ListItem("Second"));
    this.CBLienType.add(new qx.ui.form.ListItem("First & Second"));
    this.add(this.CBLienType, {row: 1, column: 3, rowSpan: 0});
    this.AddPopup ("Select to apply", this.CBLienType);

    this.add(this.CreateLoanType(), {row: 4, column: 3, rowSpan: 2});
    this.add(this.CreatePropertyType(), {row: 3, column: 5, rowSpan: 2, colSpan: 2});
    this.add(this.CreateAcceptState(), {row: 5, column: 1, rowSpan: 2});

    this.BtnCtlOk = new qx.ui.form.Button("Find My Assets", "icon/16/actions/dialog-ok.png");
    this.add(this.BtnCtlOk, {row: 5, column: 5, colSpan:0});
	this.BtnCtlOk.addListener("execute", function()
	{
	//TODO make that only one could be selected, now the last one
	//is sended
		var GBLnTp = null;
		for (var child in this.GBLoanType.getChildren())
			if(this.GBLoanType.getChildren()[child].getValue())
				GBLnTp = this.GBLoanType.getChildren()[child].getLabel();

		var GBPropSel = null;
		for (child in this.GBPropertyType.getChildren())
			if(this.GBPropertyType.getChildren()[child].getValue())
				GBPropSel = this.GBPropertyType.getChildren()[child].getLabel();

		var GBAcpSt = null;
		for (child in this.GBAcceptState.getChildren())
			if(this.GBAcceptState.getChildren()[child].getValue())
				GBAcpSt = this.GBAcceptState.getChildren()[child].getLabel();

		var data = {
			SLCorLogFraudRiskScore : this.SLCorLogFraudRiskScore.getValue(),
			SLCorLogCollRiskScore : this.SLCorLogCollRiskScore.getValue(),
			SLAcceptableFICO : this.SLAcceptableFICO.getValue(),
			SPMaxLoanAmount : this.SPMaxLoanAmount.getValue,
			SPMinLoanAmount : this.SPMinLoanAmount.getValue(),
		    SPMaxLoanToValue : this.SPMaxLoanToValue.getValue(),
		    SPMaxComLoanToValue : this.SPMaxComLoanToValue.getValue(),
		    SPMaxAdvance : this.SPMaxAdvance.getValue(),
		    CBLienType : this.CBLienType.getValue(),
			GBLoanType : GBLnTp,
		    GBPropertyType : GBPropSel,
		    GBAcceptState : GBAcpSt
		}
	    this.fireDataEvent("changeData", data);
	    this.close();
	}, this);

    this.BtnCancel = new qx.ui.form.Button("Cancel", "icon/16/actions/dialog-cancel.png");
    this.add(this.BtnCancel, {row: 5, column: 6, rowSpan:0});
  },

  members :
  {
    CtlLayout: null,
    SLCorLogFraudRiskScore: null,
    SLCorLogCollRiskScore: null,
    SLAcceptableFICO: null,

    SPMinLoanAmount: null,
    SPMaxLoanAmount: null,
    SPMaxLoanToValue: null,
    SPMaxComLoanToValue: null,
    SPMaxAdvance: null,

    CBLienType: null,

    GBLoanType: null,
    GBPropertyType: null,
    GBAcceptState: null,
  
    BtnCtrOk: null,
    BtnCancel: null,

    Filter: null,

    CreateLoanType : function()
    {
      this.GBLoanType = new qx.ui.groupbox.GroupBox();
      this.GBLoanType.setLayout(new qx.ui.layout.HBox());
      this.GBLoanType.add(new qx.ui.form.CheckBox("Fixed"));
      this.GBLoanType.add(new qx.ui.form.CheckBox("ARM"));
      //this.GBLoanType.add(new qx.ui.form.CheckBox("Hybrid"));

      this.AddPopup ("Select to apply", this.GBLoanType);

      return this.GBLoanType;
    },

    CreateAcceptState : function()
    {
      this.GBAcceptState = new qx.ui.groupbox.GroupBox();
      this.GBAcceptState.setLayout(new qx.ui.layout.Grid(4, 2));
      this.GBAcceptState.add(new qx.ui.form.CheckBox("AZ"), {row: 0, column: 0});
      this.GBAcceptState.add(new qx.ui.form.CheckBox("HI"), {row: 0, column: 1});
      this.GBAcceptState.add(new qx.ui.form.CheckBox("NV"), {row: 0, column: 2});
      this.GBAcceptState.add(new qx.ui.form.CheckBox("UT"), {row: 0, column: 3});
      this.GBAcceptState.add(new qx.ui.form.CheckBox("CA"), {row: 1, column: 0});
      this.GBAcceptState.add(new qx.ui.form.CheckBox("ID"), {row: 1, column: 1});
      this.GBAcceptState.add(new qx.ui.form.CheckBox("OR"), {row: 1, column: 2});
      this.GBAcceptState.add(new qx.ui.form.CheckBox("WA"), {row: 1, column: 3});

      this.AddPopup ("Select to apply", this.GBAcceptState);

      return this.GBAcceptState;
    },

    CreatePropertyType : function()
    {
      this.GBPropertyType = new qx.ui.groupbox.GroupBox();
      this.GBPropertyType.setLayout(new qx.ui.layout.Grid(3, 3));
      this.GBPropertyType.add(new qx.ui.form.CheckBox("SFR"), {row: 0, column: 0, rowSpan:0});
      this.GBPropertyType.add(new qx.ui.form.CheckBox("PUD"), {row: 0, column: 1, rowSpan:0});
      this.GBPropertyType.add(new qx.ui.form.CheckBox("Condo"),{row: 0, column: 2, rowSpan:0} );
      this.GBPropertyType.add(new qx.ui.form.CheckBox("Townhouse"), {row: 1, column: 0, colSpan:2});
      this.GBPropertyType.add(new qx.ui.form.CheckBox("Manufactered Housing"), {row: 1, column: 2, colSpan:0});

      this.AddPopup ("Select to apply", this.GBPropertyType);

      return this.GBPropertyType;
    }, 

    AddPopup : function(Msg, Ctl)
    {
      var popup = new qx.ui.popup.Popup(new qx.ui.layout.Canvas()).set({
        backgroundColor: "#FFFAD3",
        padding: [2, 4],
        offset : 3,
        offsetBottom : 20
      });

      popup.add(new qx.ui.basic.Atom(Msg));

      Ctl.addListener("mouseover", function(e)
      {
        popup.placeToMouse(e);
        popup.show();
      }, this);

      Ctl.addListener("mouseout", function(e)
      {
        popup.hide();
      }, this);
    }
  }

});
