const Topbar = () => {
  return (
    <div className="lc-topbar-main">
      <div id="top-bar" className="lc-topbar">
        <div className="lc-topbar-seprator"></div>
        <div className="lc-topbar-l1">
          <div className="lc-topbar-l2">
            <div className="lc-topbar-l3">
              <div className="lc-topbar-left">
                <div className="lc-topbar-col">
                  <img
                    alt="avatar"
                    src="https://cdn.livechat-files.com/api/file/lc/img/13750077/fa899ea283029a5eaec0cc5cbeae30c9.png"
                    className="lc-topbar-icon"
                  />
                </div>
                <div className="lc-online"></div>
              </div>
              <div className="lc-topbar-right">
                <div className="lc-topbar-titlebox">
                  <div className="lc-topbar-title">ChatBot</div>
                  <div className="lc-topbar-subtitle">Support Agent</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Topbar;
