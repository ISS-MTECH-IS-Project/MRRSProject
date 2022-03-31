import { FaTimes } from "react-icons/fa";
import Symptom from "./Symptom";

const Message = ({ messageIndex, message, onToggle }) => {
  return (
    <div>
      <div className="lc-massage-bot">
        <div className="lc-massage-bot-left">
          <div className="lc-massage-bot-icon">
            <img
              alt="avatar"
              src="https://cdn.livechat-files.com/api/file/lc/img/13750077/fa899ea283029a5eaec0cc5cbeae30c9.png"
              className="lc-topbar-icon"
            />
          </div>
        </div>
        <div className="lc-massage">
          <div role="row">
            <div className="lc-massage-left">
              <div
                role="gridcell"
                className="lc-massage-grid-left"
                tabIndex="-1"
              >
                <div>
                  <div className="lc-massage-title-left">
                    <span className="lc-massage-title">ChatBot </span>
                    <span className="lc-massage-title">21:25</span>
                  </div>
                </div>
                <div className="lc-massage-body-left">
                  <div className="lc-massage-body">
                    <span className="Linkify">
                      Want to see what I can do? 🤖
                    </span>
                    {/* Empty symptoms if display of symptoms is undesired */}
                    {message.hasOwnProperty("symptoms") && (
                      <Symptom symptoms={message.symptoms}></Symptom>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* user */}
      <div className="lc-massage-user">
        <div className="lc-massage">
          <div role="row">
            <div className="lc-massage-right">
              <div
                role="gridcell"
                className="lc-massage-grid-right"
                tabIndex="-1"
              >
                <div>
                  <div className="lc-massage-title-right">
                    <span className="lc-massage-title">Visitor </span>
                    <span className="lc-massage-title">21:30</span>
                  </div>
                </div>
                <div className="lc-massage-body-right">
                  <div className="lc-massage-body">
                    <span className="Linkify">hi</span>
                  </div>
                </div>
                <div className="lc-massage-read">Read</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Message;
