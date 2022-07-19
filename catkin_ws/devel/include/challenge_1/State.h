// Generated by gencpp from file challenge_1/State.msg
// DO NOT EDIT!


#ifndef CHALLENGE_1_MESSAGE_STATE_H
#define CHALLENGE_1_MESSAGE_STATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace challenge_1
{
template <class ContainerAllocator>
struct State_
{
  typedef State_<ContainerAllocator> Type;

  State_()
    : battery(0)
    , height(0.0)
    , pressure(0.0)  {
    }
  State_(const ContainerAllocator& _alloc)
    : battery(0)
    , height(0.0)
    , pressure(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _battery_type;
  _battery_type battery;

   typedef double _height_type;
  _height_type height;

   typedef double _pressure_type;
  _pressure_type pressure;





  typedef boost::shared_ptr< ::challenge_1::State_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::challenge_1::State_<ContainerAllocator> const> ConstPtr;

}; // struct State_

typedef ::challenge_1::State_<std::allocator<void> > State;

typedef boost::shared_ptr< ::challenge_1::State > StatePtr;
typedef boost::shared_ptr< ::challenge_1::State const> StateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::challenge_1::State_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::challenge_1::State_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::challenge_1::State_<ContainerAllocator1> & lhs, const ::challenge_1::State_<ContainerAllocator2> & rhs)
{
  return lhs.battery == rhs.battery &&
    lhs.height == rhs.height &&
    lhs.pressure == rhs.pressure;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::challenge_1::State_<ContainerAllocator1> & lhs, const ::challenge_1::State_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace challenge_1

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::challenge_1::State_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::challenge_1::State_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::challenge_1::State_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::challenge_1::State_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::challenge_1::State_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::challenge_1::State_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::challenge_1::State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7822bfa23aaf591dc3f18eb434eb6e41";
  }

  static const char* value(const ::challenge_1::State_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7822bfa23aaf591dULL;
  static const uint64_t static_value2 = 0xc3f18eb434eb6e41ULL;
};

template<class ContainerAllocator>
struct DataType< ::challenge_1::State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "challenge_1/State";
  }

  static const char* value(const ::challenge_1::State_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::challenge_1::State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 battery\n"
"float64 height\n"
"float64 pressure\n"
;
  }

  static const char* value(const ::challenge_1::State_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::challenge_1::State_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.battery);
      stream.next(m.height);
      stream.next(m.pressure);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct State_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::challenge_1::State_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::challenge_1::State_<ContainerAllocator>& v)
  {
    s << indent << "battery: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.battery);
    s << indent << "height: ";
    Printer<double>::stream(s, indent + "  ", v.height);
    s << indent << "pressure: ";
    Printer<double>::stream(s, indent + "  ", v.pressure);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CHALLENGE_1_MESSAGE_STATE_H