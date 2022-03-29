import { FaTimes } from "react-icons/fa";

const Message = ({ messageIndex, message, onToggle }) => {
  return (
    <div>
      <div class="lc-massage-bot">
        <div class="lc-massage-bot-left">
          <div class="lc-massage-bot-icon">
            <img
              alt="avatar"
              src="https://cdn.livechat-files.com/api/file/lc/img/13750077/fa899ea283029a5eaec0cc5cbeae30c9.png"
              class="lc-topbar-icon"
            />
          </div>
        </div>
        <div class="lc-massage">
          <div role="row">
            <div class="lc-massage-left">
              <div role="gridcell" class="lc-massage-grid-left" tabIndex="-1">
                <div>
                  <div class="lc-massage-title-left">
                    <span class="lc-massage-title">ChatBot </span>
                    <span class="lc-massage-title">21:25</span>
                  </div>
                </div>
                <div class="lc-massage-body-left">
                  <div class="lc-massage-body">
                    <span class="Linkify">Want to see what I can do? 🤖</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* user */}
      <div class="lc-massage-user">
        <div class="lc-massage">
          <div role="row">
            <div class="lc-massage-right">
              <div role="gridcell" class="lc-massage-grid-right" tabIndex="-1">
                <div>
                  <div class="lc-massage-title-right">
                    <span class="lc-massage-title">Visitor </span>
                    <span class="lc-massage-title">21:30</span>
                  </div>
                </div>
                <div class="lc-massage-body-right">
                  <div class="lc-massage-body">
                    <span class="Linkify">hi</span>
                  </div>
                </div>
                <div class="lc-massage-read">Read</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Message;
