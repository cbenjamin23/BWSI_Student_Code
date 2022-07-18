;; Auto-generated. Do not edit!


(when (boundp 'challenge_1::Flip)
  (if (not (find-package "CHALLENGE_1"))
    (make-package "CHALLENGE_1"))
  (shadow 'Flip (find-package "CHALLENGE_1")))
(unless (find-package "CHALLENGE_1::FLIP")
  (make-package "CHALLENGE_1::FLIP"))

(in-package "ROS")
;;//! \htmlinclude Flip.msg.html


(defclass challenge_1::Flip
  :super ros::object
  :slots (_direction ))

(defmethod challenge_1::Flip
  (:init
   (&key
    ((:direction __direction) "")
    )
   (send-super :init)
   (setq _direction (string __direction))
   self)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:serialization-length
   ()
   (+
    ;; string _direction
    4 (length _direction)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _direction
       (write-long (length _direction) s) (princ _direction s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _direction
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _direction (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get challenge_1::Flip :md5sum-) "326e9417def5db9a05a2704a4d8de15e")
(setf (get challenge_1::Flip :datatype-) "challenge_1/Flip")
(setf (get challenge_1::Flip :definition-)
      "string direction
")



(provide :challenge_1/Flip "326e9417def5db9a05a2704a4d8de15e")


