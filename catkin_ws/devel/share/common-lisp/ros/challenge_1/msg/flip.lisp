; Auto-generated. Do not edit!


(cl:in-package challenge_1-msg)


;//! \htmlinclude flip.msg.html

(cl:defclass <flip> (roslisp-msg-protocol:ros-message)
  ((direction
    :reader direction
    :initarg :direction
    :type cl:string
    :initform ""))
)

(cl:defclass flip (<flip>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <flip>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'flip)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name challenge_1-msg:<flip> is deprecated: use challenge_1-msg:flip instead.")))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <flip>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader challenge_1-msg:direction-val is deprecated.  Use challenge_1-msg:direction instead.")
  (direction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <flip>) ostream)
  "Serializes a message object of type '<flip>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'direction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'direction))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <flip>) istream)
  "Deserializes a message object of type '<flip>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'direction) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'direction) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<flip>)))
  "Returns string type for a message object of type '<flip>"
  "challenge_1/flip")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'flip)))
  "Returns string type for a message object of type 'flip"
  "challenge_1/flip")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<flip>)))
  "Returns md5sum for a message object of type '<flip>"
  "326e9417def5db9a05a2704a4d8de15e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'flip)))
  "Returns md5sum for a message object of type 'flip"
  "326e9417def5db9a05a2704a4d8de15e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<flip>)))
  "Returns full string definition for message of type '<flip>"
  (cl:format cl:nil "string direction~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'flip)))
  "Returns full string definition for message of type 'flip"
  (cl:format cl:nil "string direction~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <flip>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'direction))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <flip>))
  "Converts a ROS message object to a list"
  (cl:list 'flip
    (cl:cons ':direction (direction msg))
))
